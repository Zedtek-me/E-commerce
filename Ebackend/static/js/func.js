// the toggles for editing each product.
const toggleEdit= ()=>{
    let toggleArrows= document.querySelectorAll('.prod-tog')
    let editDivs= document.querySelectorAll('.edits')
    for(let count= 0; count < toggleArrows.length; count++){
        toggleArrows[count].addEventListener('click', (e)=>{
            editDivs[count].classList.toggle('edit-options');
            toggleArrows[count].classList.toggle('fa-angle-up')
            toggleArrows[count].classList.toggle('fa-angle-down')
        })
    }
}
toggleEdit()

// display a preview of product uploaded by a vendor
function preView(){
    let img_file= document.querySelector('#product_img')
    let product_img= document.querySelector('.product_img')/*image tag to hold the image for a quick display*/
    img_file.addEventListener('change', (e)=>{
        product_img.src= URL.createObjectURL(e.target.files[0])
        product_img.style.display= 'flex'
    })
}
preView()


// form submission event for product removal
function removeProd(){
    let removeBtns= document.querySelectorAll('.remove-prod')
    let formBtns= document.querySelectorAll('#removeProd')
    for(let i= 0; i < removeBtns.length; i++){
        removeBtns[i].addEventListener('click', (e)=>{formBtns[i].click()})
    }

}
removeProd()
