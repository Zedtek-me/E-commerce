// display quick links
var links= document.querySelector('.b-seller')
var arrowDown= document.querySelector('.fa-angle-down')
function displayLink(){
    links.classList.toggle('buyer-seller')
    arrowDown.classList.toggle('fa-angle-down')
    arrowDown.classList.toggle('fa-angle-up')
}

const toggleEdit= ()=>{
    let toggleArrows= document.querySelectorAll('.prod-tog')
    let editDivs= document.querySelectorAll('.edits')
    console.log(toggleArrows)
    for(let count= 0; count < toggleArrows.length; count++){
        console.log(toggleArrows.length)
        toggleArrows[count].addEventListener('click', (e)=>{
            editDivs[count].classList.toggle('edit-options');
            toggleArrows[count].classList.toggle('fa-angle-up')
            toggleArrows[count].classList.toggle('fa-angle-up')
        })
    }
}
toggleEdit()

// how it works
var detail= document.querySelector('.detail')
var detailParent= document.querySelector('.how-it-works')
const howItWorks= ()=>{
    detail.style.display= 'flex';
    setTimeout(()=>{detail.style.display='none'}, 5000)
}

// display a preview of product uploaded by a vendor
let img_file= document.querySelector('#product_img')
img_file.addEventListener('change', (e)=>{
    let product_img= document.querySelector('.product_img')/*image tag to hold the image for a quick display*/
    product_img.src= URL.createObjectURL(e.target.files[0])
}
)