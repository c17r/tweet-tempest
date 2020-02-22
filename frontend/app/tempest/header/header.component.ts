import { Component, OnInit } from '@angular/core';

import { ApiService, ITwitterInfo } from '../service/api';
import { Observable } from 'rxjs';

@Component({
    selector: 'tempest-header',
    templateUrl: './header.component.html'
})
export class TempestHeaderComponent implements OnInit {

    person$: Observable<ITwitterInfo> = this.apiService.getTwitterInfo();

    constructor(private apiService: ApiService) { }

    ngOnInit() {}

}
