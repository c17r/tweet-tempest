import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpModule, XSRFStrategy, CookieXSRFStrategy } from '@angular/http';
import { FormsModule }   from '@angular/forms';

import { 
	TempestComponent,
	TempestHeader,
	TempestForm,

	ApiService

} from './tempest';

@NgModule({

	imports:      [ 
		BrowserModule,
		HttpModule,
		FormsModule
	],

	declarations: [ 
		TempestComponent,
		TempestHeader,
		TempestForm
	],

	providers:    [
		ApiService,
		{
			provide: XSRFStrategy,
			useValue: new CookieXSRFStrategy('csrftoken', 'X-CSRFToken')
		}
	],

	bootstrap:    [ 
		TempestComponent 
	]
})
export class TempestModule { }
