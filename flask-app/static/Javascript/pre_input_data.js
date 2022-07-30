
const month = new Date();
bulan = month.getMonth()+1;
select_form = document.getElementsByName('periode');

for (var i = 0; i < 12; i++) {
    if(bulan == i+1){
    //  select_form.selectedIndex = i+1;
    //  console.log(select_form.selectedIndex);
    // document.getElementById(String(i+1)).selected = true;
    }
}
