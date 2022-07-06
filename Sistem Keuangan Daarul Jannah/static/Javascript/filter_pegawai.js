function searchBar(){
    // variables
    var input, filter, table, tr, td, i, txtValue, search_filter,search_filter_value;
    input = document.getElementById("search-txt");
    filter = input.value.toUpperCase();
    table = document.getElementById("data_pegawai");
    tr = table.getElementsByTagName("tr");
    search_filter = document.getElementById("search-bar-filter");
    search_filter_value = search_filter.options[search_filter.selectedIndex].value;
    
    // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
        if (search_filter_value == "NIP") {
            td = tr[i].getElementsByTagName("td")[0];
            if (td) {
                txtValue = td.textContent || td.innerText;
                if (txtValue.toUpperCase().indexOf(filter) > -1) {
                    tr[i].style.display = "";
                } else {
                    tr[i].style.display = "none";
                }
            }
        }
        else if (search_filter_value == "Nama") {
            td = tr[i].getElementsByTagName("td")[1];
            if (td) {
                txtValue = td.textContent || td.innerText;
                if (txtValue.toUpperCase().indexOf(filter) > -1) {
                    tr[i].style.display = "";
                } else {
                    tr[i].style.display = "none";
                }
            }
        }
        else if (search_filter_value == "Status") {
            td = tr[i].getElementsByTagName("td")[3];
            if (td) {
                txtValue = td.textContent || td.innerText;
                if (txtValue.toUpperCase().indexOf(filter) > -1) {
                    tr[i].style.display = "";
                } else {
                    tr[i].style.display = "none";
                }
            }
        }
        else if (search_filter_value == "Jabatan") {
            td = tr[i].getElementsByTagName("td")[4];
            if (td) {
                txtValue = td.textContent || td.innerText;
                if (txtValue.toUpperCase().indexOf(filter) > -1) {
                    tr[i].style.display = "";
                } else {
                    tr[i].style.display = "none";
                }
            }
        }
    }
}

function searchBarClear(){
    var searchBar = document.getElementById("search-txt");
    searchBar.value = "";
    var search_filter = document.getElementById("search-bar-filter");
    if (search_filter.value == "NIP") {
        console.log(search_filter)
        searchBar.placeholder = "Cari Berdasarkan NIP";
    }
    else if (search_filter.value == "Nama") {
        searchBar.placeholder = "Cari Berdasarkan Nama";
    }
    else if (search_filter.value == "Status") {
        searchBar.placeholder = "Cari Berdasarkan Status";
    }
    else if (search_filter.value == "Jabatan") {
        searchBar.placeholder = "Cari Berdasarkan Jabatan";
    }
    else if (search_filter.value == "Otoritas Sistem") {
        searchBar.placeholder = "Cari Berdasarkan Status";
    }
    searchBar.focus();
}

function filterOtoritas(){
     // variables
     var input, filter, table, tr, td, i, txtValue;
     input = document.getElementById("filter-otoritas");
     filter = input.value.toUpperCase();
     table = document.getElementById("data_pegawai");
     tr = table.getElementsByTagName("tr");

     // Loop through all table rows, and hide those who don't match the search query
    for (i = 0; i < tr.length; i++) {
        if (filter == "ADMIN") {
            td = tr[i].getElementsByTagName("td")[5];
            if (td) {
                txtValue = td.textContent || td.innerText;
                if (txtValue.toUpperCase().indexOf(filter) > -1) {
                    tr[i].style.display = "";
                } else {
                    tr[i].style.display = "none";
                }
            }
        }
        else if (filter == "STAFF") {
            td = tr[i].getElementsByTagName("td")[5];
            if (td) {
                txtValue = td.textContent || td.innerText;
                if (txtValue.toUpperCase().indexOf(filter) > -1) {
                    tr[i].style.display = "";
                } else {
                    tr[i].style.display = "none";
                }
            }
        }
    }
}