function addRow() {
    var rowCount = document.getElementById('myTable').rows.length;
    var table = document.getElementById("myTable");
    var row = table.insertRow(rowCount - 3);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);

    var item_name = 'item' + rowCount;
    var price_name = 'max_price' + rowCount;
 
    cell1.innerHTML = '<input type="text" name="' + item_name + '">';
    cell2.innerHTML = '<input type="text" name="' + price_name + '">';
 }
 
 function removeRow() {
    var table = document.getElementById("myTable");
    var rowCount = table.rows.length;

    // At least one row should be present (header row and submit row are not counted)
    if (rowCount > 5) {
        table.deleteRow(rowCount - 4); // Subtract 2 to skip header and submit rows
    } else {
        alert("Cannot delete the first row.");
    }
}


function openNewTab(item, price) {
    window.open(`/display_results/${item}?max_price=${price}`, "_blank");
    return true;
}

