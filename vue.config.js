module.exports = {
  transpileDependencies: ["vuetify"],
  devServer: {
    proxy: {
      "/api": {
        target: "http://localhost:4000",
        secure: true,
        pathRewrite: {
          "^/api": "/api"
        }
      }
    }
  }
};
