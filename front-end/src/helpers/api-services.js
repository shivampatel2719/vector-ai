import Axios from 'axios';

export const getColumns = async () => {
    let result =  await getCards();
    let returnArr = [];
    result.forEach((e) => returnArr.push(e));
    return returnArr;
}
  
export const getCards = () => {
    return new Promise((resolve,reject) => {
        Axios.get("http://127.0.0.1:6969/")
        .then((res) => {
        resolve(res.data);
        })
        .catch((err) => {
        reject(err);
        })
    });
}

export const swapCards = (data) => {
    let {id1,id2} = data;
    Axios.patch(`http://127.0.0.1:6969/position/${id1}/${id2}`);
    // Axios.patch(`http://127.0.0.1:6969/position/${id2}/${id1}`);
}
