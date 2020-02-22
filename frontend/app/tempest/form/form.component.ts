import { Component, Input, OnInit } from '@angular/core';
import { debounce, trim } from 'lodash';

import { ApiService, ITweetTempest } from '../service/api';

@Component({
    selector: 'tempest-form',
    templateUrl: './form.component.html'
})
export class TempestFormComponent {

    readonly tweetLength = 140;
    peeps = '';
    tweetCount = true;
    startCount = 1;
    message = '';
    result: ITweetTempest[] = [];
    processInput = debounce(this.parseTweets, 300);
    disableSend = true;

    constructor(private apiService: ApiService) {}

    sendTweets(): void {
        this.apiService.sendTweetTempest(this.result)
            .then(data => {

            });
    }

    parseTweets(): void {
        let count = this.startCount || 1;
        let pk = 1;
        let prefix = '';
        const result: ITweetTempest[] = [];
        let size = 0;
        let raw = trim(this.message);

        while (raw.length > 0) {

            prefix = this.peeps ? this.peeps + ' ' : '';
            if (this.tweetCount) {
                prefix = `${prefix}${count}/ `;
            }

            size = this.tweetLength - prefix.length;

            while (raw.length > size && raw.charAt(size) !== ' ' && size > 0) {
                size--;
            }

            result.push({
                pk,
                text: prefix + raw.substring(0, size)
            });

            if (size > raw.length) {
                raw = '';
            } else {
                raw = trim(raw.substring(size));
            }

            count++;
            pk++;
        }

        this.result = result;
        this.disableSend = this.result.length === 0;
    }
}
