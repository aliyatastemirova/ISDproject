$("document").ready(function ($) {

    var nav = $('header');

    $(window).scroll(function () {
        if ($(this).scrollTop() > 55) {
            nav.addClass("sticky");
        } else {
            nav.removeClass("sticky");
        }
    });

    //select js

    $('select').each(function () {
        var $this = $(this), numberOfOptions = $(this).children('option').length;
        $this.addClass('select-hidden');
        $this.wrap('<div class="select"></div>');
        $this.after('<div class="select-styled"></div>');

        var $styledSelect = $this.next('div.select-styled');
        $styledSelect.text($this.children('option').eq(0).text());

        var $list = $('<ul />', {
            'class': 'select-options'
        }).insertAfter($styledSelect);

        for (var i = 0; i < numberOfOptions; i++) {
            $('<li />', {
                text: $this.children('option').eq(i).text(),
                rel: $this.children('option').eq(i).val()
            }).appendTo($list);
        }

        var $listItems = $list.children('li');

        $styledSelect.click(function (e) {
            e.stopPropagation();
            $('div.select-styled.active').not(this).each(function () {
                $(this).removeClass('active').next('ul.select-options').hide();
            });
            $(this).toggleClass('active').next('ul.select-options').toggle();
        });

        $listItems.click(function (e) {
            e.stopPropagation();
            $styledSelect.text($(this).text()).removeClass('active');
            $this.val($(this).attr('rel'));
            $list.hide();
            //console.log($this.val());
        });

        $(document).click(function () {
            $styledSelect.removeClass('active');
            $list.hide();
        });
    });

    // faq lists accordion
    $('.accordion-lists li h4').click(function () {
        $(this).next('p').slideToggle();
        $(this).toggleClass('active');
        $('.accordion-lists li h4').not(this).next('p').slideUp();
        $('.accordion-lists li h4').not(this).removeClass('active');

    });
    // counter js
    $('.counter').counterUp({
        delay: 10,
        time: 1000
    });
    $(function () {
        $("#course-carousel, #popular-carousel, #masters-carousel").owlCarousel({

            //Basic Speeds
            slideSpeed: 300,
            paginationSpeed: 650,

            //Autoplay
            autoPlay: true,
            goToFirst: true,
            goToFirstSpeed: 1000,

            // Navigation
            navigation: true,
            navigationText: ["<i class='fa fa-chevron-left'></i>", "<i class='fa fa-chevron-right'></i"],
            pagination: false,


            // Responsive
            responsive: true,
            items: 4,
            itemsDesktop: [1199, 4],
            itemsDesktopSmall: [980, 3],
            itemsTablet: [768, 2],
            itemsMobile: [479, 1]


        });
        $("#testimonial-carousel").owlCarousel({

            //Basic Speeds
            slideSpeed: 300,
            paginationSpeed: 650,

            //Autoplay
            autoPlay: true,
            goToFirst: true,
            goToFirstSpeed: 1000,

            // Navigation

            pagination: true,
            paginationNumbers: true,

            // Responsive
            responsive: true,
            items: 1,
            itemsDesktop: [1199, 1],
            itemsDesktopSmall: [980, 1],
            itemsTablet: [768, 1],
            itemsMobile: [479, 1]


        });
    });

    $(function () {
        var btnContainer = document.getElementById("nav-tab");
        // Get all buttons with class="btn" inside the container
        if (btnContainer !== null) {
            var btns = btnContainer.getElementsByClassName("nav-item");

            // Loop through the buttons and add the active class to the current/clicked button
            for (var i = 0; i < btns.length; i++) {
                btns[i].addEventListener("click", function() {
                var current = document.getElementsByClassName("active");

                // If there's no active class
                if (current.length > 0) {
                    current[0].className = current[0].className.replace(" active", "");
                }

                // Add the active class to the current/clicked button
                this.className += " active";
                });
            }
        }

    });

});
