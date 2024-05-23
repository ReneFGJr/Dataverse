import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RepatriationComponent } from './repatriation.component';

describe('RepatriationComponent', () => {
  let component: RepatriationComponent;
  let fixture: ComponentFixture<RepatriationComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [RepatriationComponent]
    });
    fixture = TestBed.createComponent(RepatriationComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
