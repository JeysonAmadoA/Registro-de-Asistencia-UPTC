import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SystemsEngineerComponent } from './systems-engineer.component';

describe('SystemsEngineerComponent', () => {
  let component: SystemsEngineerComponent;
  let fixture: ComponentFixture<SystemsEngineerComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [SystemsEngineerComponent]
    });
    fixture = TestBed.createComponent(SystemsEngineerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
