/** module3
 *  script.js
 *  Created by Mauro J. Pappaterra on 22 of October 2017.
 */

$( document ).ready(function() {

    $("#button").click( function(){

        var row = $("#row").val();
        var pancakes = row.length
        var k = $("#k").val();
        var flag = true;

        for (var i = 0; i < pancakes; i++) {
            if (!(row[i] == 'x' || row[i] == 'o')){
                flag = false;
            };
        }

        if ($.isNumeric(k) && k > 1 && k <= row.length && flag){

            var goto = $(location).attr('href')+ row + k;

            var goto = goto.replace('?','/') // workaround for ? in address bar

            window.open(goto)

        } else {
            alert("Invalid Input: Enter a row of pancakes x (for happy) and o (for flat)" +
                " (e.g.: xooxoxoxox) and an integer larger than 1 but not larger than the total" +
                " number of pancakes on the given row");
        }

        e.preventDefault();
        });

    $("#close").click( function(){
            window.close();
        });
});
