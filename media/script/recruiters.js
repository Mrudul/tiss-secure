(function($){
    jQuery(function(){
        jQuery("#our_recruiters").scrollable({
          size: 4,
          speed: 800,
          easing: 'easeInOutQuint'
        })
        .autoscroll({
            steps: 2,
            interval: 800
        })
        .circular();
    });
})(jQuery);

