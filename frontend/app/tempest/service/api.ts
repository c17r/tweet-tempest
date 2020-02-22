import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { shareReplay } from 'rxjs/operators';

export interface ITwitterInfo {
    profile_image_url: string;
    screen_name: string;
    characters_reserved_per_media: string;
}

interface ITwitterInfoResponse {
    response: ITwitterInfo;
}

export interface ITweetTempest {
    pk: number;
    text: string;
}

@Injectable({
    providedIn: 'root',
})
export class ApiService {

    constructor(private http: HttpClient) { }

    getTwitterInfo(): Observable<ITwitterInfo> {
        return new Observable<ITwitterInfo>((obs) => {
            this.http.get<ITwitterInfoResponse>('/api/twitter/info/')
                .subscribe(
                    (data) => {
                        obs.next(data.response);
                        obs.complete();
                    },
                    (err) => {
                        this.handleError(err);
                        obs.complete();
                    }
                );
        }).pipe(shareReplay(1));
    }

    sendTweetTempest(tweets: ITweetTempest[]) {
        console.log(tweets);
        return this.http.post('/api/twitter/tweet/', JSON.stringify(tweets))
            .toPromise()
            .then(this.unwrapReponse)
            .catch(this.handleError);
    }

    private unwrapReponse(response) {
        const body = response.json();
        return body.response || {};
    }

    private handleError(error): void {
        const errorMsg = (error.message)
            ? error.message
            : error.status
                ? `${error.status} - ${error.statusText}`
                : 'Server Error';

        alert(errorMsg);
    }

}
