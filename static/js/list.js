jQuery(function ($) {
    $('.movie-list').jscroll({
        loadingHtml: '<img src="' + settings.STATIC_URL + 'img/loading.gif" alt="Loading" />',
        padding: 100,
        pagingSelector: '.pagination',
        nextSelector: 'a.next-page:last',
        contentSelector: '.item, .pagination'

    })
})