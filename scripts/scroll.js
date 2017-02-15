jQuery(window).scroll(function(){
   var fromTopPx1 = 600;
   var fromTopPx2 = 1800;
   var scrolledFromtop = jQuery(window).scrollTop();
   if((scrolledFromtop > fromTopPx1) && (scrolledFromtop < fromTopPx2)){
      jQuery('html').addClass('scrolled1');
      jQuery('html').removeClass('scrolled2');
      jQuery('html').removeClass('top');
   }else if(scrolledFromtop > fromTopPx2){
      jQuery('html').addClass('scrolled2');
      jQuery('html').removeClass('scrolled1');
      jQuery('html').removeClass('top');
   }else{
      jQuery('html').addClass('top');
      jQuery('html').removeClass('scrolled1');
      jQuery('html').removeClass('scrolled2');
   }
});
