import { Component, Input, OnInit } from '@angular/core';
import _ from 'lodash';

import {ApiService} from '../service/api';

@Component({
	selector: 'tempest-form',
	templateUrl: './form.component.html'
})
export class TempestForm implements OnInit {
	
	constructor(apiService: ApiService) {
        this.apiService = apiService;
		this.peeps = '';
		this.tweet_count = true;
		this.start_count = 1;
		this.message = '';
		this.result = [];
		this.processInput = _.debounce(this.parseTweets, 300)
		this.allowSend = false;
	}

	ngOnInt() {
	}

	sendTweets() {
        this.apiService.sendTweetTempest(this.result)
            .then(data => {

            })
	}

	parseTweets() {
		var count = this.start_count || 1;
		var pk = 1;
		var prefix = '';
		var result = [];
		var size = 0;
		var raw = _.trim(this.message);
		var piece = '';

		while (raw.length > 0) {
			piece = '';

			prefix = this.peeps ? this.peeps + ' ' : '';
			if (this.tweet_count)
				prefix = `${prefix}${count}/ `;

			size = 140 - prefix.length;

			while(raw.length > size && raw.charAt(size) != ' ' && size > 0)
				size--;

			result.push({
				pk: pk,
				text: prefix + raw.substring(0, size)
			});

			if (size > raw.length)
				raw = '';
			else
				raw = _.trim(raw.substring(size));

			count++;
			pk++;
		}
		this.result = result;
        this.allowSend = (this.result.length != 0);
	}
}
