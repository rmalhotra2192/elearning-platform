import axios from "axios";
export default {
  login(store, router, data) {
    axios({
      method: "post",
      url: "http://" + location.hostname + ":8000/token",
      data: data,
      headers: {
        "Content-Type": "multipart/form-data",
      },
    })
      .then((response) => {
        let access_token = response["data"]["access_token"];
        let token_type = response["data"]["token_type"];
        let header = {
          Authorization: this.capitalize(token_type) + " " + access_token,
        };

        console.log(header);

        axios({
          method: "get",
          url: "http://" + location.hostname + ":8000/users/me/",
          headers: header,
        }).then((response) => {
          let user = response;
          console.log(user);
          console.log(access_token);
          let payload = {
            user: user,
            access_token: access_token,
            token_type: this.capitalize(token_type),
          };
          store.dispatch("login", payload);

          router.push({ name: "courses" });
        });
      })
      .catch(function (response) {
        alert("Login Failed!. Please try again with valid credentials.");
        console.log(response);
      });
  },
  register(router, data) {
    axios({
      method: "post",
      url: "http://" + location.hostname + ":8000/register",
      data: data,
    })
      .then((response) => {
        console.log(response);
        router.push({ name: "login" });
      })
      .catch(function (response) {
        console.log(response);
      });
  },
  capitalize(s) {
    return s && s[0].toUpperCase() + s.slice(1);
  },
};
