import { Injectable } from '@angular/core';
import { Http, Response } from '@angular/http';
import 'rxjs/add/operator/toPromise';

@Injectable()
export class ApiService {

	constructor(http: Http) {
		this.http = http;
	}

	getTwitterInfo() {
		return this.http.get('/api/twitter/info/')
            .toPromise()
            .then(this._unwrapReponse)
            .catch(this._handleError);
	}

	sendTweetTempest(tweets) {
		console.log(tweets);
		return this.http.post('/api/twitter/tweet/', JSON.stringify(tweets))
            .toPromise()
            .then(this._unwrapReponse)
            .catch(this._handleError);
	}

	_unwrapReponse(response) {
		let body = response.json();
		return body.response || {};
	}

	_handleError(error) {
		let errorMsg = (error.message) ? error.message : error.status ? `${error.status} - ${error.statusText}` : 'Server Error';
		alert(errorMsg);
		return Promise.reject(errorMsg);
	}

}
