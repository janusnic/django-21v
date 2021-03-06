from django import forms
from django.contrib import admin
from ckeditor.widgets import CKEditorWidget

from blog.models import Category, Post, UserProfile, Comment, Slide, Slider, Page

from redactor.widgets import RedactorEditor

# Register your models here.

def make_published(modeladmin, request, queryset):
    queryset.update(status='1')
make_published.short_description = "Mark selected stories as published"

#class PostAdminForm(forms.ModelForm):
#    body = forms.CharField(widget=CKEditorWidget())
#
#    class Meta:
#        model = Post
#        fields = "__all__" 


class PostAdminForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
           'body': RedactorEditor(),
        }

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'status','updated')
    search_fields = ['title']
    date_hierarchy = 'updated'
    ordering = ['title']
    actions = [make_published, 'make_draft','make_unpublished']
    form = PostAdminForm

    def make_unpublished(self, request, queryset):
        rows_updated = queryset.update(status='2')
        if rows_updated == 1:
            message_bit = "1 story was"
        else:
            message_bit = "%s stories were" % rows_updated
        self.message_user(request, "%s successfully marked as unpublished." % message_bit)
    make_unpublished.short_description = "Mark selected stories as unpublished"
    
    def make_draft(self, request, queryset):
        queryset.update(status='0')
    make_draft.short_description = "Mark selected stories as draft"

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

class CommentAdmin(admin.ModelAdmin):
    list_display = ["post", "author", "created"]

class SlideInline(admin.TabularInline):
    model = Slide
    extra = 1


class SliderAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    inlines = [SlideInline, ]


# Page


class PageAdmin(admin.ModelAdmin):
    content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Page
        fields = '__all__'

admin.site.register(Page, PageAdmin)


admin.site.register(Slider, SliderAdmin)



#admin.site.register(Post, PostAdmin)
admin.site.register(UserProfile)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Post, PostAdmin)

admin.site.register(Comment, CommentAdmin)