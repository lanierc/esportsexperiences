export const setToken = token => {
  localStorage.setItem("vueBlogToken", token);
};

export const getToken = () => {
  return localStorage.getItem("vueBlogToken");
};

export const removeToken = () => {
  localStorage.removeItem("vueBlogToken");
};
