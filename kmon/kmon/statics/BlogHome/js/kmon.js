// Agency Theme JavaScript

(function($) {
    // jQuery for page scrolling feature - requires jQuery Easing plugin
    $('.search').bind('click', function(event) {
        var input = $(".search-text>input");
        if(input.val() != "")
            location.href = '/blog/search/'+input.val();
    });
    $('.search-text>input').keydown(function(event) {
        if(event.keyCode == 13){
            if( $(this).val() != "" ){
            location.href = '/blog/search/'+$(this).val();
            }
        }
    });

})(jQuery); 
