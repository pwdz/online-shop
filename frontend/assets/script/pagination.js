var productInfos = {}
get();
async function get(){
    try {

        let formBody = [];
        // for (const property in loginData) {
        //     const encodedKey = encodeURIComponent(property);
        //     const encodedValue = encodeURIComponent(loginData[property]);
        //     formBody.push(encodedKey + "=" + encodedValue);
        // }
        formBody = formBody.join("&");

        const res = await fetch('http://127.0.0.1:5000/products/list', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
            }
            // body: formBody
        })
        const resData = await res.json()
        console.log(resData);
        if (resData.success) {
            console.log(resData.data)
            // text = "ورود موفقیت آمیز است";
            // textColor = "green";
        }
        else {
            // text = "اطلاعات وارد شده معتبر نمی باشد";

        }
    } catch (error) {
        console.log(error);
    }

}