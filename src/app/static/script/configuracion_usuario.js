const $filePicker = document.querySelector("#filePicker"),
$imagePreview = document.querySelector("#imagePreview");

$filePicker.addEventListener("change", () => {
const files = $filePicker.files;
if (!files || !files.length) {
    $imagePreview.src = "default.jpg";
    return;
}
const firstFile = files[0];
const objectURL = URL.createObjectURL(firstFile);

$imagePreview.src = objectURL;
});
const $opencl = document.getElementById("lose-open"),
$asa = document.getElementById("profileTwo"),
$as = document.getElementById("backGround")
$opencl.addEventListener("click",()=>{
$asa.classList.toggle("displasment")
$as.classList.toggle("displasment")
})
const $openc = document.getElementById("cancel")
$openc.addEventListener("click",()=>{
    $asa.classList.toggle("displasment")
    $as.classList.toggle("displasment")
    })