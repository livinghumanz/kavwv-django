$(window).on("load",function() {
    $(window).scroll(function() {
      var windowBottom = $(this).scrollTop() + $(this).innerHeight();
      $(".Lcade, .Rcade").each(function() {
        /* Check the location of each desired element */
        var objectBottom = $(this).offset().top + $(this).outerHeight();
        
        /* If the element is completely within bounds of the window, fade it in */
        if (objectBottom < windowBottom) { //object comes into view (scrolling down)
          if ($(this).css("opacity")==0) {$(this).fadeTo(500,1);}
        } else { //object goes out of view (scrolling up)
          if ($(this).css("opacity")==1) {$(this).fadeTo(500,0);}
        }
      });
    }).scroll(); //invoke scroll-handler on page-load
    Internship();
  });

//when completed loaded
  window.addEventListener('DOMContentLoaded', (event) => {
    // navbar effect......
	var navb = document.getElementById("navb").style;
	navb.position="static";
});
window.onscroll = function() {isInViewport(document.getElementById("Tstack"),document.getElementById("Footer"))};
//function to execute effect
function isInViewport(element,Footer) {
	
  const Frect = Footer.getBoundingClientRect();
	const rect = element.getBoundingClientRect();
	//debugging of window element
	/*console.log(
        "Frec-top: "+Frect.top,
        "Frec-left :"+Frect.left,
		"Frect-bottom :"+Frect.bottom,
		"window in height :"+window.innerHeight+" and "+document.documentElement.clientHeight,
		Frect.right,"window in width :"+window.innerWidth+" and "+document.documentElement.clientWidth
	);*/
	var navb = document.getElementById("navb").style;
	if(rect.bottom<0 && navb.position=="static"){ navb.position = "fixed";}
	else if(rect.bottom>0 && navb.position=="fixed") {navb.position="static";}
  
  //-----------------Managing the display of Down arrow--------------
  if (Frect.top<=window.innerHeight) {
    $(".section").css("display","none");
  } else {
    $(".section").css("display","block");
  }
}

/*---------------------change style on resize window----------------*/
$(window).resize(function(){Internship();});

function Internship() {
  var width=window.outerWidth;
  //console.log("width-> "+width);
  if(width >= 870){
    $(".nav").find('a').css('width','auto');
    $(".nav").css('max-width','750px');
    //console.log("\n Iam in "+width);
  }
  else{
    $(".nav").find('a').css('width','100px');
    $(".hauto").css('width','auto');
    $(".nav").css('max-width','350px');
   // console.log("\n Iam out "+width);
  }
  
}























