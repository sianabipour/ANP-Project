(function ($) {
"use strict";

// meanmenu
$('#mobile-menu').meanmenu({
	meanMenuContainer: '.mobile-menu',
	meanScreenWidth: "991"
});

$(window).on('scroll', function () {
	var scroll = $(window).scrollTop();
	if (scroll < 200) {
		$(".header-sticky").removeClass("sticky");
	} else {
		$(".header-sticky").addClass("sticky");
	}
});

//mobile side menu
$('.side-toggle').on('click', function () {
	$('.side-info').addClass('info-open');
	$('.offcanvas-overlay').addClass('overlay-open');
})

$('.side-info-close,.offcanvas-overlay').on('click', function () {
	$('.side-info').removeClass('info-open');
	$('.offcanvas-overlay').removeClass('overlay-open');
});

// Search Header
$('.ns-header-action-search').on('click', function() {
	$('body').addClass('search-active');
})
$(".ba-search-popup .ba-color-layer").on("click", function () {
	$("body").removeClass("search-active");
});

function sliderActive() {
	/*------------------------------------
	Slider
	--------------------------------------*/
	if (jQuery(".slider-active").length > 0) {
		let sliderActive1 = '.slider-active';
		let sliderInit1 = new Swiper(sliderActive1, {
			// Optional parameters
			slidesPerView: 1,
			rtl: false,
			slidesPerColumn: 1,
			paginationClickable: true,
			loop: true,

			autoplay: {
				delay: 3000,
			},

			// If we need pagination
	        pagination: {
				el: ".cinkes-swiper-pagination",
				clickable: true,
			},

			// Navigation arrows
			navigation: {
				nextEl: '.slider-swiper-next',
				prevEl: '.slider-swiper-prev',
			},

			a11y: false
		});

		function animated_swiper(selector, init) {
			let animated = function animated() {
				$(selector + ' [data-animation]').each(function () {
					let anim = $(this).data('animation');
					let delay = $(this).data('delay');
					let duration = $(this).data('duration');

					$(this).removeClass('anim' + anim)
						.addClass(anim + ' animated')
						.css({
							webkitAnimationDelay: delay,
							animationDelay: delay,
							webkitAnimationDuration: duration,
							animationDuration: duration
						})
						.one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function () {
							$(this).removeClass(anim + ' animated');
						});
				});
			};
			animated();
			// Make animated when slide change
			init.on('slideChange', function () {
				$(sliderActive1 + ' [data-animation]').removeClass('animated');
			});
			init.on('slideChange', animated);
		}

		animated_swiper(sliderActive1, sliderInit1);
	}}

	
/* magnificPopup img view */
$('.popup-image').magnificPopup({
	type: 'image',
	gallery: {
	  enabled: true
	}
});
/* magnificPopup video view */
$('.popup-video').magnificPopup({
	type: 'iframe'
});

$('.has-nice-select, .product__filter-count select, .has-nice-select-2').niceSelect();

// data background
$("[data-background]").each(function(){
	$(this).css("background-image","url("+$(this).attr("data-background") + ") ")
})
// data width
$("[data-width]").each(function(){
	$(this).css("width",$(this).attr("data-width"))
})
// data background color
$("[data-bg-color]").each(function(){
	$(this).css("background-color",$(this).attr("data-bg-color"))
})
//for menu active class
$('.portfolio_nav button').on('click', function(event) {
	$(this).siblings('.active').removeClass('active');
	$(this).addClass('active');
	event.preventDefault();
});

// scrollToTop
$.scrollUp({
	scrollName: 'scrollUp', // Element ID
	topDistance: '300', // Distance from top before showing element (px)
	topSpeed: 300, // Speed back to top (ms)
	animation: 'fade', // Fade, slide, none
	animationInSpeed: 200, // Animation in speed (ms)
	animationOutSpeed: 200, // Animation out speed (ms)
	scrollText: '<i class="icofont icofont-long-arrow-up"></i>', // Text for element
	activeOverlay: false, // Set CSS color to display scrollUp active point, e.g '#00FFFF'
});


// service active 
const serviceActive = new Swiper(".service-active-2", {
	slidesPerView: 4,
	spaceBetween: 30,
	loop: true,
	autoplay: {
		delay: 3000,
	},
	navigation: {
		nextEl: ".sg-service-prev",
		prevEl: ".sg-service-next",
		},
		breakpoints: {
		0: {
			slidesPerView: 1,
			},
		576: {
			slidesPerView: 1,
		},
		768: {
			slidesPerView: 2,
		},
		992: {
			slidesPerView: 3,
		},
		1199: {
			slidesPerView: 3
		},
		1299: {
			slidesPerView: 3
		},
		1399: {
			slidesPerView: 4
		}
	}
});


// team active 
const teamActive = new Swiper(".team-active", {
	slidesPerView: 2,
	spaceBetween: 30,
	loop: true,
	speed: 2000,
	autoplay: {
		delay: 3000,
	},
	navigation: {
		nextEl: ".sg-portfolio-prev",
		prevEl: ".sg-portfolio-next",
		},
		breakpoints: {
		0: {
			slidesPerView: 1,
			},
		576: {
			slidesPerView: 2,
		},
		768: {
			slidesPerView: 2,
		},
		992: {
			slidesPerView: 2,
		},
		1200: {
			slidesPerView: 2
		}
	}
});

// team active 
const teamActiveTwo = new Swiper(".team-active-2", {
	slidesPerView: 4,
	spaceBetween: 30,
	loop: true,
	autoplay: {
		delay: 3000,
	},
	navigation: {
		nextEl: ".sg-portfolio-prev",
		prevEl: ".sg-portfolio-next",
		},
		breakpoints: {
		0: {
			slidesPerView: 1,
			},
		576: {
			slidesPerView: 2,
		},
		768: {
			slidesPerView: 2,
		},
		992: {
			slidesPerView: 3,
		},
		1200: {
			slidesPerView: 3,
		},
		1400: {
			slidesPerView: 4,
		}
	}
});


// sidebar blog active
const sidebarBlogActive = new Swiper(".sidebar-blog-active", {
	slidesPerView: 1,
	spaceBetween: 0,
	loop: true,
	speed: 2000,
	autoplay: {
		delay: 3000,
	},
	pagination: {
		el: ".sidebar-blog-pagination",
		clickable: true,
	},
		breakpoints: {
		0: {
			slidesPerView: 1,
			},
		576: {
			slidesPerView: 1,
		},
		768: {
			slidesPerView: 1,
		},
		992: {
			slidesPerView: 1,
		},
		1199: {
			slidesPerView: 1
		}
	}
});


// testimonial active
const testimonialActive = new Swiper(".testimonial-active", {
	slidesPerView: 1,
	spaceBetween: 0,
	loop: true,
	speed: 2000,
	autoplay: {
		delay: 3000,
	},
	navigation: {
		nextEl: ".testimonial-swiper-next",
		prevEl: ".testimonial-swiper-prev",
		},
		breakpoints: {
		0: {
			slidesPerView: 1,
			},
		576: {
			slidesPerView: 1,
		},
		768: {
			slidesPerView: 1,
		},
		992: {
			slidesPerView: 1,
		},
		1199: {
			slidesPerView: 1
		}
	}
});

// video active
const videoActive = new Swiper(".video-active", {
	slidesPerView: 1,
	spaceBetween: 30,
	loop: false,
	speed: 2000,
	autoplay: {
		delay: 3000,
	},
	breakpoints: {
		0: {
			slidesPerView: 1,
			},
		576: {
			slidesPerView: 1,
		},
		768: {
			slidesPerView: 1,
		},
		992: {
			slidesPerView: 1,
		},
		1199: {
			slidesPerView: 1
		}
	}
});

// portfolio active 
const portfolioActive = new Swiper('.portfolio-active', {
	spaceBetween: 10,
	loop: false,
	loopedSlides: 5,
	slidesPerView: 1,
	autoplay: {
		delay: 3000,
	},
	breakpoints: {
		0: {
			slidesPerView: 1,
			},
		576: {
			slidesPerView: 1,
		},
		768: {
			slidesPerView: 1,
		},
		992: {
			slidesPerView: 1,
		},
		1199: {
			slidesPerView: 1
		}
	}
});
const portfolioThumbs = new Swiper('.portfolio-thumbs', {
	centeredSlides: true,
	slidesPerView: 'auto',
	touchRatio: 0.2,
	slideToClickedSlide: true,
	loop: false,
	slidesPerView: 5,
	navigation: {
		nextEl: '.portfolio-swiper-prev',
		prevEl: '.portfolio-swiper-next',
	},
	breakpoints: {
		0: {
			slidesPerView: 2,
			},
		576: {
			slidesPerView: 2,
		},
		768: {
			slidesPerView: 3,
		},
		992: {
			slidesPerView: 3,
		},
		1200: {
			slidesPerView: 5
		}
	}
});
portfolioActive.controller.control = portfolioThumbs;
portfolioThumbs.controller.control = portfolioActive;


// banner active 
const bannerActive = new Swiper('.banner-active', {
	spaceBetween: 0,
	loop: true,
	loop: true,
	loopedSlides: 1,
	slidesPerView: 1,
	allowTouchMove:false,
	autoplay: {
		delay: 3000,
	},
	navigation: {
		nextEl: '.banner-swiper-next',
		prevEl: '.banner-swiper-prev',
	},
	breakpoints: {
		0: {
			slidesPerView: 1,
			},
		576: {
			slidesPerView: 1,
		},
		768: {
			slidesPerView: 1,
		},
		992: {
			slidesPerView: 1,
		},
		1199: {
			slidesPerView: 1
		}
	}
});
const bannerThumbs = new Swiper('.banner-thumbs', {
	centeredSlides: true,
	slidesPerView: 1,
	touchRatio: 0.2,
	slideToClickedSlide: true,
	allowTouchMove:false,
	loop: true,
	slidesPerView: 1,
	
	breakpoints: {
		0: {
			slidesPerView: 1,
			},
		576: {
			slidesPerView: 1,
		},
		768: {
			slidesPerView: 1,
		},
		992: {
			slidesPerView: 1,
		},
		1199: {
			slidesPerView: 1
		}
	}
});
bannerActive.controller.control = bannerThumbs;
bannerThumbs.controller.control = bannerActive;

//   odometer
$('.choose_count').appear(function (e) {
	var odo = $(".choose_count");
	odo.each(function () {
		var countNumber = $(this).attr("data-count");
		$(this).html(countNumber);
	});
});

// WOW active
new WOW().init();

sliderActive();

// product quantity
var productQuantity = 1;

// quantity form 
$('.single-product-quantity-box .plus').on('click', function () {
	var selectedInput = $(this).closest('.single-product-quantity-box').find('input');
	productQuantity += 1;
	selectedInput.attr('value', productQuantity);
});
$('.single-product-quantity-box .minus').on('click', function () {
	var selectedInput = $(this).closest('.single-product-quantity-box').find('input');
	productQuantity-=1;
	if(productQuantity < 1) {
		productQuantity = 1;
	}
	selectedInput.attr('value', productQuantity);
});


// InHover Active 
$('.location-common').on('mouseenter', function () {
	$(this).addClass('active').parent().siblings().find('.location-common').removeClass('active');
});


$('.progress_one').rProgressbar({
	percentage: 85,
	fillBackgroundColor: '#006464',
    backgroundColor: '#fff',
	duration: 3000,
	height: '8px',
	borderRadius: '4px',
}); 
$('.progress_two').rProgressbar({
	percentage: 96,
	fillBackgroundColor: '#006464',
    backgroundColor: '#fff',
	duration: 4000,
	height: '8px',
	borderRadius: '4px',
}); 
$('.progress_three').rProgressbar({
	percentage: 90,
	fillBackgroundColor: '#006464',
    backgroundColor: '#fff',
	duration: 5000,
	height: '8px',
	borderRadius: '4px',
}); 

$('.progress_one_two').rProgressbar({
	percentage: 85,
	fillBackgroundColor: '#153730',
    backgroundColor: '#cfd9d7',
	duration: 3000,
	height: '8px',
	borderRadius: '4px',
}); 
$('.progress_two_two').rProgressbar({
	percentage: 96,
	fillBackgroundColor: '#153730',
    backgroundColor: '#cfd9d7',
	duration: 4000,
	height: '8px',
	borderRadius: '4px',
}); 
$('.progress_three_two').rProgressbar({
	percentage: 90,
	fillBackgroundColor: '#153730',
    backgroundColor: '#cfd9d7',
	duration: 5000,
	height: '8px',
	borderRadius: '4px',
}); 


})(jQuery);