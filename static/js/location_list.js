jQuery(function ($) {
    var $popup = $('#popup');

    $('body').on('click', '.item a', function (e) {
        console.log("link click");
        e.preventDefault();
        var $link = $(this);
        var popup_url = $link.data('popup-url');
        var popup_title = $link.data('popup-title');
        if (!popup_url) {
            return true;
        }
        $('.modal-title', $popup).html(popup_title);
        $('.modal-body', $popup).load(popup_url, function () {
            $popup.on('shown.bs.modal', function () {
                console.log("on dialog shown");
            }).modal("show");
        });
        $('.close', $popup).click(function () {
            console.log("on dialog close");
        })
    })
});


//$(document).ready(function () {
//
//});