var searchData= []
token= document.cookie.split('=')[1]
const searchProd=()=>{
    let searchInput= document.querySelector('[name=search-term]')
    let searchIcon= document.querySelector('.fa-magnifying-glass')
    let searchQuery= document.querySelector('[name=query]')
    let submitBtn =document.querySelector('#submit-btn')

    searchIcon.addEventListener('click', async (e)=>{
        if(searchInput.value !== '' && searchInput.value !== null){// check whether anything was given to be searched
           searchQuery.value= searchInput.value //insert the search query into the input btn of the submitting form
           searchInput.value= ''// turn the search widget into empty
           submitBtn.click()// click the submit button to submit the search
        }//end if
    })
}

searchProd()