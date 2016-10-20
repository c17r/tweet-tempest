import { Component } from '@angular/core';

import { ApiService } from '../service/api';

@Component({
	selector: 'tempest-header',
	templateUrl: './header.component.html'
})
export class TempestHeader implements OnInit { 
	constructor(apiService: ApiService) {
		this.apiService = apiService;
		this.person = {
            screen_name: '',
            profile_image_url: ''
        };
	}

	ngOnInit() {
		this.apiService.getTwitterInfo()
            .then(data => this.person = data)
	}
}
