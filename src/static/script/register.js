window.addEventListener('load' , function(){
    new Glider(document.querySelector('.caruserl_lista'),{
        slidesToShow: 4,
        slidesToScroll: 4,
        draggable: false,
        dots: '.carusel_ind',
        arrows: {
          prev: '.carusser_anterior',
          next: '.carusser_siguiente'
        }
    })
})