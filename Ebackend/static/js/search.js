var searchData= []
token= document.cookie.split('=')[1]
const searchProd=()=>{
    let searchInput= document.querySelector('[name=search-term')
    let searchIcon= document.querySelector('.fa-magnifying-glass')

    searchIcon.addEventListener('click', async (e)=>{
        searchItem= searchInput.value //get search data
        searchInput.value= '' //empty search box

        if(searchItem){// check whether anything was given to be searched
            let response= await fetch('search/', {
                method: 'POST',
                body: JSON.stringify(searchItem),
                'headers': {
                    'Content-Type': 'application/json',
                    'X-CSRFToken' : token
                }
            })//end fetch
            let data= response.json()
            console.log(data)
        }//end if
    })
}
// const returnSearch= async()=>{
//     let s= await searchProd()
//     return s
// }

// returnSearch()
searchProd()