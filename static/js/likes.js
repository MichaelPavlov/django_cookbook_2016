(function ($) {
    $(document).on('click', '.like-button', function () {
        var $button = $(this);
        var $badge = $button.closest('.like-widget').find('.like-badge');
        var caption = '';
        $.post($button.data('href'), function (data) {
            if (data['action'] == 'added') {
                caption = $button.data('unlike-text');
                $button.addClass('active').html(
                    '<span class="glyphicon glyphicon-star"></span> ' + caption
                )
            } else {
                caption = $button.data('like-text');
                $button.removeClass('active').html(
                    '<span class="glyphicon glyphicon-star-empty"></span> ' + caption
                )
            }
            $badge.html(data['count']);
        }, 'json');
    });
})(jQuery);