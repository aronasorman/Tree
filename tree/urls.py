from django.conf.urls import patterns, include, url
from django.conf import settings
from first.views import load , gen_url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mytree.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/$', include(admin.site.urls)),
    url(r'^gen_url/$', gen_url),
)

urlpatterns += patterns('',
	url(r'^stories-and-literature/fairy-tales/little-red-riding-hood/$', load ,{'addr' : 'little-red-riding-hood'}  ),
	url(r'^stories-and-literature/fairy-tales/emperors-new-clothes/$', load ,{'addr' : 'emperors-new-clothes'}  ),
	url(r'^stories-and-literature/fairy-tales/boy-who-cried-wolf/$', load ,{'addr' : 'boy-who-cried-wolf'}  ),
	url(r'^stories-and-literature/fairy-tales/$', load ,{'addr' : 'fairy-tales'}  ),
	url(r'^stories-and-literature/classic-literature/chinese-literature/tao-te-ching/$', load ,{'addr' : 'tao-te-ching'}  ),
	url(r'^stories-and-literature/classic-literature/chinese-literature/five-rings/$', load ,{'addr' : 'five-rings'}  ),
	url(r'^stories-and-literature/classic-literature/chinese-literature/$', load ,{'addr' : 'chinese-literature'}  ),
	url(r'^stories-and-literature/classic-literature/european-literature/don-quixote/$', load ,{'addr' : 'don-quixote'}  ),
	url(r'^stories-and-literature/classic-literature/european-literature/divina-commedia/$', load ,{'addr' : 'divina-commedia'}  ),
	url(r'^stories-and-literature/classic-literature/european-literature/$', load ,{'addr' : 'european-literature'}  ),
	url(r'^stories-and-literature/classic-literature/indian-literature/shulba-sutras/$', load ,{'addr' : 'shulba-sutras'}  ),
	url(r'^stories-and-literature/classic-literature/indian-literature/shakuntala/$', load ,{'addr' : 'shakuntala'}  ),
	url(r'^stories-and-literature/classic-literature/indian-literature/mahabharata/$', load ,{'addr' : 'mahabharata'}  ),
	url(r'^stories-and-literature/classic-literature/indian-literature/$', load ,{'addr' : 'indian-literature'}  ),
	url(r'^stories-and-literature/classic-literature/$', load ,{'addr' : 'classic-literature'}  ),
	url(r'^stories-and-literature/$', load ,{'addr' : 'stories-and-literature'}  ),
)
#Done