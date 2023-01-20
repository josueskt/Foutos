function Comprobar() {
    
    //alert((document.getElementById("ppp").value=="2"));
 
  if (document.getElementById("descrip").value=="") {
    alert("Llene el campo Descripcion")
    return false;
  }
  if (document.getElementById("titul").value=="") {
    alert("Ingrese un titulo"); 
    return false;
  }
  if (document.getElementById("image").value=="") {
    alert("Ingrese una imagen"); 
    return false;
  }
  return true;
  }

 
