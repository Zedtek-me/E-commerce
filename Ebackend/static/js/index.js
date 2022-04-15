// displaying product form db
// const productDisplay= ()=>{
//     let parentCont= document.querySelector('.root-parent')
//     fetch(`product/`)
//     .then((res)=>{return res.json()})
//     .then((prod)=>{prod.map((i, item)=>{
//         // 
//         let section= document.createElement('SECTION')
//         let productCont=document.createElement('DIV')
//         let productName= document.createElement('H4')
//         let productImg= document.createElement('IMG')
//         productImg.src= i.product_image
//         productName.textContent= i.product_name
//         productCont.appendChild(productImg)
//         productCont.appendChild(productName)
//         section.appendChild(productCont)
//         parentCont.appendChild(section)
//         console.log(section)
//     })})
// }

// productDisplay()

// display quick links
var links= document.querySelector('.b-seller')
var arrowDown= document.querySelector('.fa-angle-down')
function displayLink(){
    links.classList.toggle('buyer-seller')
    arrowDown.classList.toggle('fa-angle-down')
    arrowDown.classList.toggle('fa-angle-up')
}


// "how it works"--> a hover effect that displays how a product works
var detail= document.querySelector('.detail')
var detailParent= document.querySelector('.how-it-works')
const howItWorks= ()=>{
    detail.style.display= 'flex';
    setTimeout(()=>{detail.style.display='none'}, 5000)
}

// details about the cart functionality
var addToCart= document.querySelectorAll('.add-to-cart')/*the add to cart parent */
var cart_detail= document.querySelectorAll('.cart-detail')/*the details when hover */
for(let j= 0; j<addToCart.length; j++){
    addToCart[j].addEventListener('mouseover', (e)=>{
        cart_detail[j].style.display='flex';
        setTimeout(()=>{cart_detail[j].style.display='none'}, 5000)})
        };

console.log(typeof addToCart.childItem)
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
let img_file= document.querySelector('#product_img')
let product_img= document.querySelector('.product_img')/*image tag to hold the image for a quick display*/
img_file.addEventListener('change', (e)=>{
    product_img.src= URL.createObjectURL(e.target.files[0])
    product_img.style.display= 'flex'
}
)

// form submission event for product removal
let removeBtns= document.querySelectorAll('.remove-prod')
let formBtns= document.querySelectorAll('#removeProd')
for(let i= 0; i < removeBtns.length; i++){
    removeBtns[i].addEventListener('click', (e)=>{
       formBtns[i].click()
    })
}

