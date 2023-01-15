window.addEventListener('load' , function(){
    new Glider(document.querySelector('.caruserl_lista'),{
        slidesToShow: 4,
        slidesToScroll: 2,
        draggable: false,
        dots: '.carusel_ind',
        arrows: {
          prev: '.carusser_anterior',
          next: '.carusser_siguiente'
        }
    })
})

const $openclose = document.getElementById("close-open"),
$userclose = document.getElementById("closesecsion")
$openclose.addEventListener("click",()=>{
  $userclose.classList.toggle("close")
})


const $openclos = document.getElementById("pen-clo"),
$userclos = document.getElementById("closesecsion_two")
$openclos.addEventListener("click",()=>{
  $userclos.classList.toggle("close_two")
})



