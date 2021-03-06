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

//displays the product update form
const updateProd= ()=>{
    let editBtns= document.querySelectorAll('.edit-prod')
    let cancelBtns= document.querySelectorAll('.cancel')
    let editConts= document.querySelectorAll('.remove-nd-edit')
    for(let i= 0; i< editBtns.length; i++){
        editBtns[i].addEventListener('click', (e)=>{
            editConts[i].style.display= 'flex'
        })//end of first event listener, for display
        cancelBtns[i].addEventListener('click',(e)=>{
            editConts[i].style.display= 'none'
        })//end of second event listener to undisplay
    }
}
updateProd()

// for profile settings
const toggleSetting= ()=>{
    let [settingsCont, settingArrow, settingsForm]= [document.querySelector('#update-account-txt'), document.querySelector('.settings-tog'), document.querySelector('#acc-update-form')]
    settingsCont.addEventListener('click', (e)=>{
        settingArrow.classList.toggle('fa-angle-down')
        settingArrow.classList.toggle('fa-angle-up')
        if (settingsForm.style.display=='flex'){
            settingsForm.style.display = 'none'
        }
        else{
            settingsForm.style.display= 'flex'
        }
    })
}

toggleSetting()