import re
from django.template.defaultfilters import stringfilter
from django.template import defaultfilters
from django.core.mail import send_mail
import settings
import datetime

def add_helpful_classes(form):
        for name,field in form.fields.iteritems():
                new_classes = (type(field).__name__, type(field.widget).__name__, field.required and "Required" or "Optional")
                if 'class' in field.widget.attrs:
                        field.widget.attrs['class'] = " ".join(field.widget.attrs['class'].split().extend(new_classes))
                else:
                        field.widget.attrs['class'] = " ".join(new_classes)

# not quite sure where to put this code
def parsewords(curobj,fieldname='language'):
    """
    Returns a set of words contained in fieldname
    """
    DELIMITERS = u'(,| and |et\.?al\.?)'
    STOPWORDS = set(['',',','and','et.al.','et.al','etal','others'])
    STRIPLIST = ('.',',')
    
    unique_words = list()
    curstr = unicode(eval('curobj.'+fieldname))
    curwords = re.split(DELIMITERS,curstr)
    for word in curwords:
        cleanword = word.strip()
        while cleanword.startswith(STRIPLIST) or cleanword.endswith(STRIPLIST):
            for stripchar in STRIPLIST:
                cleanword = cleanword.strip(stripchar)
        if (cleanword not in unique_words) and (cleanword not in STOPWORDS):
            unique_words.append(cleanword)

    unique_words.sort()
    return unique_words

# Get the old slugifier
old_slugify = defaultfilters.slugify
def translat_slugify(str):
	char_translat = { 
		("а","А","ә","Ә",) : "a",
		("б","Б",) : "b",
		("в","В",) : "v",
		("г","Г","ғ","Ғ",) : "g",
		("д","Д",) : "d",
		("е","Е",) : "e",
		("ё","Ё",) : "e",
		("ж","Ж",) : "j",
		("з","З",) : "z",
		("и","И","і","І",) : "i",
		("й","Й",) : "y",
		("к","К","қ","Қ",) : "k",
		("л","Л",) : "l",
		("м","М",) : "m",
		("н","Н","ң","Ң",) : "n",
		("о","О","ө","Ө",) : "o",
		("п","П",) : "p",
		("р","Р",) : "r",
		("с","С",) : "s",
		("т","Т",) : "t",
		("у","У","ү","Ү","ұ","Ұ",) : "u",
		("ф","Ф",) : "f",
		("х","Х","һ","Һ",) : "h",
		("ц","Ц",) : "c",
		("ч","Ч",) : "ch",
		("ш","Ш",) : "sh",
		("щ","Щ",) : "sh",
		("ъ","Ъ",) : "",
		("ы","Ы",) : "i",
		("ь","Ь",) : "",
		("э","Э",) : "e",
		("ю","Ю",) : "yu",
		("я","Я",) : "ya",
	}
	for chars,trans in char_translat.items():
		for char in chars:
			str = str.replace(char.decode('utf-8'),trans) 
	return old_slugify(str)

# "Overwrite" the old slugify
#defaultfilters.slugify = translat_slugify

#def slugify(value):
#import unicodedata
#value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
#value = unicode(re.sub('[^\w\s\-\+]', '', value).strip().lower())
#return re.sub('[\-\+\s]+', '-', value)

@stringfilter
def slugify(value):
	return translat_slugify(value)[0:50]
#slugify = stringfilter(slugify)


def send_mails(subscribers, subject, message):
    # we don't use send_mass_mail as we don't want to leak other users email addresses
    for s in subscribers:
        if not s.bookmark:
            now=datetime.datetime.now()
            # only send out things once every 60 seconds 
            if now-s.last_updated > datetime.timedelta(0, 60):
                send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [ s.user.email ],fail_silently=True)
                s.last_updated=now
                s.save()
