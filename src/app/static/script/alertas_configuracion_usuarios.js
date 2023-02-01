
function Comprobar() {
    
    //alert((document.getElementById("ppp").value=="2"));
 
  if (document.getElementById("nombre").value=="") {
    alert("Ingrese su nombre"); 
    return false;
  }
  if (document.getElementById("nombre").value.length<5) {
    alert("El nombre debe tener al menos 5 caracteres"); 
    return false;
  }
  if (document.getElementById("email").value=="") {
    alert("Ingrese un email valido"); 
    return false;
  
  }
  if (document.getElementById("pais").value=="1") {
    alert("Debes seleccionar un país");
    return true;
    
}
  return true;
}
