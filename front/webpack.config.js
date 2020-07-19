const webpack = require('webpack');
const HtmlWebpackPlugin = require('html-webpack-plugin')

const htmlPlugin = new HtmlWebpackPlugin({
  template: "./index.html",
  filename: "./index.html"
});

module.exports = {
  mode: "development",
  entry: "./src/index.tsx",
  output: {
    path: `${__dirname}/dist`,
    filename: "main.js"
  },
  module: {
    rules: [
      {
        test: /\.tsx?$/,
        use: "ts-loader"
      },
      {
        test: /\.scss$/,
        loaders: [
          'style-loader',
          'css-loader?modules',
          'sass-loader'
        ],
      }
    ]
  },
  resolve: {
    extensions: [".ts", ".tsx", ".js", ".json"]
  },
  plugins: [
    htmlPlugin,
    new webpack.HotModuleReplacementPlugin()
  ]
};