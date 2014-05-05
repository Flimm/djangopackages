from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns("",
    url(
        regex=r"^grids/$",
        view=views.grid_list,
        name="grid_list",
    ),
    url(
        regex=r"^grids/(?P<slug>[-\w]+)/$",
        view=views.grid_detail,
        name="grid_detail",
    ),
    url(
        regex=r"^packages/(?P<slug>[-\w]+)/$",
        view=views.package_detail,
        name="package_detail",
    ),
    url(
        regex=r"^categories/(?P<slug>[-\w]+)/$",
        view=views.category_detail,
        name="category_detail"
    ),
    url(
        regex=r"^users/(?P<github_account>[-\w]+)/$",
        view=views.user_detail,
        name="user_detail"
    )
)
