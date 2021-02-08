
(function($) {
    'use strict';

    // Main Navigation
    $( '.hamburger-menu' ).on( 'click', function() {
        $(this).toggleClass('close');
        $('.site-branding').toggleClass('hide');
        $('.site-navigation').toggleClass('show');
        $('.site-header').toggleClass('no-shadow');
    });

})(jQuery);



$("a[href='#scroll_top']").click(function() {
    $("html, body").animate({ scrollTop: 0 }, "slow");
    return false;
  });