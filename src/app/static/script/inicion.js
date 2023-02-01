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


function test(imagen , titulo ,descripcion) {
  
  const  node = document.getElementById("datos")
  node.innerHTML = ''
  let def =  "<img src='./static/img/todos/"+imagen+"' width =  '400px' alt=''>"
  let tit = "<h1>"+titulo+"</h1>"
  let desc = "<p>"+descripcion+"</p>"
  //let textnode = document.createElement(def)
  document.getElementById("datos_titulo").innerHTML = tit
  document.getElementById("datos").innerHTML = def
  document.getElementById("datos_descripcion").innerHTML = desc
  //llamada a la base de datos pasandole el id
  // 
 
}



