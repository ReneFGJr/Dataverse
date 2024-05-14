import { Component } from '@angular/core';
import { TranslateService } from '@ngx-translate/core';
import { lastValueFrom } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent {
  title = 'Dataverse-SPAdmim';
  DOI = ''
  currentLanguage: string = 'pt_BR';

  async ngOnInit(): Promise<void> {
    await this.setLanguage();
  }

  async setLanguage(): Promise<void> {
    //const ipInfo$ = this.apiService.getIPInfo();
    this.translate.setDefaultLang('pt');
  }

  constructor(private translate: TranslateService) {
    translate.setDefaultLang('pt');
  }

  switchLanguage(language: string) {
    this.translate.use(language);
  }

  hello(data: string) {
    console.log(data);
    this.DOI = data
  }
}
