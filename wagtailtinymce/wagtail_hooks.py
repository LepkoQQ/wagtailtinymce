from django.templatetags.static import static
from django.utils.html import format_html, format_html_join

from wagtail.wagtailadmin.templatetags.wagtailadmin_tags import hook_output
from wagtail.wagtailcore import hooks


@hooks.register('insert_editor_css')
def insert_editor_css():
    css_files = [
        'wagtailtinymce/css/icons.css'
    ]
    css_includes = format_html_join(
        '\n',
        '<link rel="stylesheet" href="{0}">',
        ((static(filename),) for filename in css_files),
        )
    return css_includes + hook_output('insert_tinymce_css')


@hooks.register('insert_editor_js')
def insert_editor_js():
    js_files = [
        'wagtailtinymce/js/vendor/tinymce/tinymce.min.js',
        'wagtailtinymce/js/tinymce-plugins/tinymce-wagtaillink.js',
        'wagtailtinymce/js/rich-text-editor.js',
    ]
    js_includes = format_html_join(
        '\n',
        '<script src="{0}"></script>',
        ((static(filename),) for filename in js_files)
        )
    return js_includes + hook_output('insert_tinymce_js')


@hooks.register('insert_tinymce_js')
def images_richtexteditor_js():
    js_files = [
        'wagtailtinymce/js/tinymce-plugins/tinymce-wagtailimage.js',
    ]
    js_includes = format_html_join(
        '\n',
        '<script src="{0}"></script>',
        ((static(filename),) for filename in js_files)
        )
    return js_includes + format_html(
        """
        <script>
            registerMCEPlugin('wagtailimage');
            registerMCEButton('wagtailimage');
        </script>
        """,
    )


@hooks.register('insert_tinymce_js')
def embeds_richtexteditor_js():
    return format_html(
        '<script src="{0}"></script>'
        '<script>'
        'registerMCEPlugin("noneditable");'
        'registerMCEPlugin("wagtailembeds");'
        'registerMCEButton("wagtailembeds");'
        '</script>',
        static('wagtailtinymce/js/tinymce-plugins/tinymce-wagtailembeds.js'),
        )


@hooks.register('insert_tinymce_js')
def docs_richtexteditor_js():
    js_files = [
        'wagtailtinymce/js/tinymce-plugins/tinymce-wagtaildoclink.js',
    ]
    js_includes = format_html_join(
        '\n',
        '<script src="{0}"></script>',
        ((static(filename),) for filename in js_files)
        )
    return format_html(
        """
        <script>
            registerMCEPlugin('wagtaildoclink');
            registerMCEButton('wagtaildoclink');
        </script>
        """,
        static('wagtailtinymce/images/icon-document.png')
    ) + js_includes