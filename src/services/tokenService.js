export const setToken = (token) => {
  localStorage.setItem("esxToken", token);
};

export const getToken = () => {
  return localStorage.getItem("esxToken");
};

export const removeToken = () => {
  localStorage.removeItem("esxToken");
};
