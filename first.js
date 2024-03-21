let boxes = document.querySelectorAll(".box");

let turn = true;


function initializeBox(boxes){
    boxes.forEach(
        (box) => {
            box.innerText = "-";
        }
    );
}

function isMatchingTriplets(boxes, index, symbol){
    return boxes[index].innerText == symbol &&
    boxes[index+1].innerText == symbol &&
    boxes[index+2].innerText == symbol; 
}

function isMatchingTripletsVerticle(boxes, index, symbol){
    return boxes[index].innerText == symbol &&
    boxes[index+3].innerText == symbol &&
    boxes[index+6].innerText == symbol; 
}

function isMatchingDiagonals(boxes, symbol){
    return (boxes[0].innerText == symbol && boxes[4].innerText == symbol && boxes[8].innerText == symbol)
    || (boxes[2].innerText == symbol && boxes[4].innerText == symbol && boxes[6].innerText == symbol);
}

function isWinner(boxes, symbol){
    for(let i=0; i<9; i=i+3){
        if(isMatchingTriplets(boxes, i, symbol)){
            return true;
        }
    }
    for(let i=0; i<3; i++){
        if(isMatchingTripletsVerticle(boxes, i, symbol)){
            return true;
        }
    }
    if(isMatchingDiagonals(boxes, symbol)){
        return true;
    }

    return false;
}


initializeBox(boxes);

boxes.forEach(
    (box) => {
        box.addEventListener("click", () => {
            if(turn){
                box.innerText = "X";
                if(isWinner(boxes, "X")){
                    alert("X wins.")
                }
            }
            else{
                box.innerText = "O";
                if(isWinner(boxes, "O")){
                    alert("O wins.")
                }
            }
            turn = !turn;
        });
    }
);


