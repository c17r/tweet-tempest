var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');
var lodashPlugin = require('lodash-webpack-plugin');

module.exports = {
	context: __dirname,

	entry: {
		vendor: ['webpack-dev-server/client?http://0.0.0.0:3000','webpack/hot/only-dev-server','./frontend/js/vendor'],
		main:   ['webpack-dev-server/client?http://0.0.0.0:3000','webpack/hot/only-dev-server','./frontend/js/index'],
	},

	output: {
		path: path.resolve('./frontend/bundles/'),
		filename: '[name].[hash].js',
		chunkFilename: '[id].[hash].chunk.js',
		publicPath: 'http://localhost:3000/frontend/bundles/',
	},

	plugins: [
		new webpack.NoErrorsPlugin(),
		new lodashPlugin(),
		new webpack.optimize.OccurenceOrderPlugin(),
		new webpack.optimize.CommonsChunkPlugin({name: ['main', 'vendor'], 'minChunks': Infinity}),
		new webpack.HotModuleReplacementPlugin(),
		new BundleTracker({filename: './webpack-stats.json',}),
	],

	module: {
		loaders: [
			{ 
				test: /\.jsx?$/, 
				exclude: /node_modules/, 
				loaders: ['babel', 'angular2-template-loader'],
			},

			{
				test: /\.html$/,
				loader: 'html',
			},
		],
	},

	resolve: {
		modulesDirectories: ['node_modules', 'bower_components'],
		extensions: ['', '.js', '.jsx'],
	},
}