import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { MainComponent } from './010_tools/page/main/main.component';
import { RepatriationComponent } from './010_tools/page/repatriation/repatriation.component';

const routes: Routes = [
  { path: '', component: MainComponent },
  { path: 'tools/repatriation', component: RepatriationComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
