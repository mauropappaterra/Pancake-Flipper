/** module3
 *  script.js
 *  Created by Mauro J. Pappaterra on 22 of October 2017.
 */

$( document ).ready(function() {

    $("#button").click( function(){

        var row = $("#row").val().toLowerCase();
        var pancakes = row.length
        var k = $("#k").val();
        var flag = true;

        row = row.replace(/\+/g , "x");
        row = row.replace(/-/g , "o");

        for (var i = 0; i < pancakes; i++) {
            if (!(row[i] == 'x' || row[i] == 'o')){
                flag = false;
            };
        }

        if ($.isNumeric(k) && k > 1 && k <= row.length && flag){

            var url = $(location).attr('href')+ row + k;
            url = url.replace('?','/') // workaround for ? in address bar

            window.open(url)

        } else {
            alert("Invalid Input: Enter a row of pancakes + (for happy) and - (for flat)" +
                " (e.g.: +--+++--+--+) and an integer larger than 1 but not larger than the total" +
                " number of pancakes on the given row");
        }
        });

    $("#close").click( function(){
            window.close();
        });
});
